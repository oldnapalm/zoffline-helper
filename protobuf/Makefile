all:
	protoc --python_out=. activity.proto
	protoc --python_out=. login.proto
	protoc --python_out=. profile.proto
	protoc --python_out=. per-session-info.proto
	protoc --python_out=. udp-node-msgs.proto

clean:
	rm -f *_pb2.py *_pb2.pyc
