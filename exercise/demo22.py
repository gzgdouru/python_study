#coding:utf-8
'''
两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单
'''

numB = ["x", "y", "z"]

for a in numB:
    for b in numB:
        for c in numB:
            if a != "x" and c not in ("x", "z"):
                tmp = [a, b, c]
                if len(set(tmp)) == 3:
                    print "a->%s b->%s c->%s" % (a, b, c)