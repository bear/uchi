import os
from dotenv import load_dotenv
from app import create_app


dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument(
        "-p",
        "--port",
        default=5000,
        type=int,
        help="port to listen on",
    )
    args = parser.parse_args()
    port = args.port

    app = create_app()
    app.run(host="0.0.0.0", port=port)
