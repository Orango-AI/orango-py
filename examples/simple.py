from dotenv import load_dotenv

from orango import OrangoExecutionResult, Sandbox

load_dotenv()

def run():
    sandbox = Sandbox()
    sandbox.exec('x = 1')

    execution = sandbox.exec('x += 1; x')
    if isinstance(execution, OrangoExecutionResult):
        print(execution.result)  # outputs 2

    sandbox.close()

if __name__ == '__main__':
    run()
