'''
元组的坑
'''

if __name__ == "__main__":
    t = (1, 2, [30, 40])

    try:
        # t[2] += [59, 60]
        t[2].extend([59, 60])
    except:
        print("except: ", t)
    else:
        print("normal: ", t)