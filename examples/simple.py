from orango import OrangoExecutionResult, Sandbox


def run():
    sandbox = Sandbox.create()
    sandbox.exec('x = 1')

    execution = sandbox.exec('x += 1; x')
    if isinstance(execution, OrangoExecutionResult):
        print(execution.result)  # outputs 2

    sandbox.close()

if __name__ == '__main__':
    run()
