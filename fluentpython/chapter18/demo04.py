'''
tqdm使用
'''
from tqdm import tqdm
import time

if __name__ == "__main__":
    for i in tqdm(range(100)):
        time.sleep(0.01)

    pbar = tqdm(["a", "b", "c", "d"])
    for char in pbar:
        time.sleep(0.25)
        pbar.set_description("Processing %s" % char)
