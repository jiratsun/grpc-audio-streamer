# gRPC Audio Streamer
gRPC Audio Streamer is a gRPC server that stream a pre-recorded set of audio in order specified by `text` to the client. 

Delay between streamed audio chunks can also be included to simulate processing delay.

## Dependencies
Dependencies are listed in `requirements.txt`; they can be installed using `pip install -r requirements.txt`.

Additionally, to compile a new `.proto`, the `grpcio-tools` package is needed.

## Usage
To start, run Server1.py and Client1.py.

Delay can be adjusted in Server1.py.

The server can be accessed using your web browser through http://localhost:8000/.

Example:
```
http://localhost:8000/tts?text=01233210
text: sequence of indices, each number correspond to an audio file in recordings
```