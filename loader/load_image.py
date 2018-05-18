import os
import paramiko
import glob
import gc
import multiprocessing
import os


def load_image_into_RAM(path, name, number):
    """Load images into ram, and return array"""
    assert os.path.exists(path),AssertionError("No such PATH")
    assert os.path.exists(path+name), AssertionError("No such file")
    assert int(number), ValueError("Number not int!")
    image_path = [os.path.join(path, name+'{}.png'.format(i)) for i in range(1, number)]
    return image_path


def load_file_from_server(host, port):
    """Load file from server, host - string host adr, port - int port
    localpath and remotepath init in function and don't change yet, same like username and password"""
    transport = paramiko.Transport((host, port))
    transport.connect(username='login', password='password')
    sftp = paramiko.SFTPClient.from_transport(transport)
    remotepath = '/path/to/remote/file.py'
    localpath = '/path/to/local/file.py'
    sftp.get(remotepath, localpath)

    sftp.close()
    transport.close()
#Две функции можно объединить дописав флаг, пока что этого делать не нужно - это ухудшит читабельность кода


def load_file_to_server(host, port):
    """Put some file to server host, port, localpath, remotepath - work's like load_file_from_server"""
    transport = paramiko.Transport((host, port))
    transport.connect(username='login', password='password')
    sftp = paramiko.SFTPClient.from_transport(transport)
    remotepath = '/path/to/remote/file.py'
    localpath = '/path/to/local/file.py'
    sftp.put(localpath, remotepath)
    sftp.close()
    transport.close()


def clean_dir(path):
    """Clean dir after detection"""
    assert os.path.exists(path), AssertionError("No such PATH")
    files = glob.glob(path)
    for i in files:
        os.remove(i)
    print("Dir empty!")


def clean_ram():
    """Clean RAM"""
    gc.collect()
    return True


def clean_gpu_memory(func, args):
    assert os.path.exists(args), AssertionError("No such dir!")
    p = multiprocessing.Process(target=func, args=args)
    p.start()
    p.join()


if __name__ == "__main__":
    clean_dir("google")
