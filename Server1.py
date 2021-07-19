from multiprocessing import Process, Queue, Manager
from concurrent import futures

import grpc
import test1_pb2_grpc
import test1_pb2

import time
import pydub
import ffmpy

NUM_OF_WORKERS = 2
files = ["num0", "num1", "num2", "num3", "num4", "num5", "num6", "num7", "num8", "num9"]
folder = "normalized\\"
format = ".mp3"
p = pydub.AudioSegment
workers = []
sampleRate = 48000
bitsPerSample = 16
channels = 1
delay = 2

class Worker(Process):
    def __init__(self, identifier, queue):
        "Initialize a worker process"
        Process.__init__(self)
        self.identifier = identifier
        self.queue = queue

    def process(self, word, i, result):
        "Insert index:file_name into result"
        index = int(word)

        ff = ffmpy.FFmpeg(inputs={"recordings\\" + files[index] + ".wav": None},
        outputs={folder + files[index] + format: ["-filter:a", "loudnorm=I=-20:TP=-1.5:LRA=11:measured_I=-23.54:measured_TP=-7.96:measured_LRA=0.00:measured_thresh=-34.17:linear=true", "-y"]})
        ff.run()
        time.sleep(delay) #Delay

        result[i] = files[index]

    def run(self):
        "Overide Process.run()"
        while True:
            try:
                word, i, result = self.queue.get(timeout = 0.05)
                self.process(word, i , result)
            except:
                pass

class AudioStreamingServicer(test1_pb2_grpc.AudioStreamingServicer):
    def __init__(self) -> None:
        "Initialize servicer"
        super().__init__()

    def GetAudio(self, request, context):
        "Stream audio"
        global manager
        global queue

        result = manager.dict()
    
        text = request.text

        lst = list(text)
        length = len(lst)
        
        for i in range(length):
            "Insert word into workers' queue"
            word = lst[i]
            queue.put([word, i, result])

        for i in range(length):
            "Yield audio in order"
            while i not in result:
                "Wait for the ith file to finish processing"
                time.sleep(0.05)
           
            audio = p.from_file(folder + result[i] + format).raw_data
            if i == 0:
                audio = genHeader(sampleRate, bitsPerSample, channels) + audio
            
            yield test1_pb2.Audio(audio = audio)

def genHeader(sampleRate, bitsPerSample, channels):
    "Return .wav header"
    datasize = 2000*10**6
    o = bytes("RIFF",'ascii')                                               # (4byte) Marks file as RIFF
    o += (datasize + 36).to_bytes(4,'little')                               # (4byte) File size in bytes excluding this and RIFF marker
    o += bytes("WAVE",'ascii')                                              # (4byte) File type
    o += bytes("fmt ",'ascii')                                              # (4byte) Format Chunk Marker
    o += (16).to_bytes(4,'little')                                          # (4byte) Length of above format data
    o += (1).to_bytes(2,'little')                                           # (2byte) Format type (1 - PCM)
    o += (channels).to_bytes(2,'little')                                    # (2byte)
    o += (sampleRate).to_bytes(4,'little')                                  # (4byte)
    o += (sampleRate * channels * bitsPerSample // 8).to_bytes(4,'little')  # (4byte)
    o += (channels * bitsPerSample // 8).to_bytes(2,'little')               # (2byte)
    o += (bitsPerSample).to_bytes(2,'little')                               # (2byte)
    o += bytes("data",'ascii')                                              # (4byte) Data Chunk Marker
    o += (datasize).to_bytes(4,'little')                                    # (4byte) Data size in bytes
    return o

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers = 10))
    test1_pb2_grpc.add_AudioStreamingServicer_to_server(AudioStreamingServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    manager = Manager()
    queue = Queue()
    for i in range(NUM_OF_WORKERS):
        w = Worker(i, queue)
        w.start()
        workers.append(w)

    serve()