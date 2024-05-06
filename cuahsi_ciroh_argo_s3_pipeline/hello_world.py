import dvc.api

params = dvc.api.params_show()

if __name__ == "__main__":  # pragma: no cover
    message = params['hello_world']['message']
    with open('output.txt', 'w') as f:
        f.write(message)
        
