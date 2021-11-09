from app import app
from app.wrappers import TVMazeAPI


if __name__ == '__main__':
    app.run()


@app.shell_context_processor
def make_context():
    return {
        'client': TVMazeAPI()
    }