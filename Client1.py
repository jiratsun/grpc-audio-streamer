from flask import Flask, request, Response

import grpc
import test1_pb2_grpc
import test1_pb2

app = Flask(__name__)

channel = grpc.insecure_channel("localhost:50051")
stub = test1_pb2_grpc.AudioStreamingStub(channel)

def generator(req):
    "Yield audio chunks"
    for response in stub.GetAudio(req):
        yield response.audio 

@app.route("/tts", methods = ["GET"])
def tts():  
    text = request.args.get("text")
    req = test1_pb2.Text(text = text)
    
    return Response(generator(req), mimetype = "audio/wav")

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 8000)
    channel.close()