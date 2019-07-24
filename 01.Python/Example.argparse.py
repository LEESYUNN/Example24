import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--port", type=int, default=None, help="example_port.")

parser.add_argument("--model_name", type=str, default=None, help="example_model.")

if __name__ == '__main__': 

    # python Example.argparse.py --port=8080 --model_name=unicode
    args = parser.parse_args()

    print(args.port)
    print(args.model_name)
