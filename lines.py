###########################
# lines.py
#
# class to automate getting
# and formatting lines
###########################
from datetime import datetime
import feedparser

def find_nth_pivot(str_in, str_search, n):
    cur = 0
    p = -1
    while cur<n:
        temp = str_in[p+1:].find(str_search)
        if temp == -1:
            return -1
        p += 1 + temp
        cur += 1
    return p

class Lines:
    def __init__(self, url='http://www.referincome.com/odds/rss2/football_nfl.xml'):
        self.d = feedparser.parse(url)

    def lines(self):
        ll = []
        l_double_names = ['New', 'Green', 'San', 'Tampa', 'Los', 'Kansas']
        for e in self.d['entries']:
            str_title = e['title'].split()
            t1 = str_title[0]
            if t1 in l_double_names:
                if str_title[1] == 'York-A':
                    t1 = t1 + ' York Jets'
                elif str_title[1] == 'York-N':
                    t1 = t1 + ' York Giants'
                else:
                    t1 = t1 + ' ' + str_title[1]
                spread = str_title[2]
                t2 = str_title[7]
                if t2 in l_double_names:
                    if str_title[8] == 'York-A':
                        t2 = t2 + ' York Jets'
                    elif str_title[8] == 'York-N':
                        t2 = t2 + ' York Giants'
                    else:
                        t2 = t2 + ' ' + str_title[8]
            else:
                spread = str_title[1]
                t2 = str_title[6]
                if t2 in l_double_names:
                    if str_title[7] == 'York-A':
                        t2 = t2 + ' York Jets'
                    elif str_title[7] == 'York-N':
                        t2 = t2 + ' York Giants'
                    else:
                        t2 = t2 + ' ' + str_title[7]
            if spread[0] != '-':
                spread = '+' + spread
            pivot = find_nth_pivot(e['title'], '(', 3) + 1
            str_date = e['title'][pivot:-1]
            try:
                game_time = datetime.strptime(str_date, '%b %d, %Y %I:%M %p')
            except:
                continue
            tup = (t1, spread, t2, game_time)
            ll.append(tup)
        return ll

    def print_for_fb(self):
        ll = self.lines()
        for l in ll:
            if l[3].isoweekday()==1 or (l[3].isoweekday()==7 and l[3].hour > 17) or l[3].isoweekday()==4:
                print(l[0], l[1], '@', l[2] , ' -> Prime')
            else:
                print(l[0], l[1], '@', l[2])

    def store_lines(self):
        ll = self.line()


if __name__ == "__main__":
    l = Lines()
    l.print_for_fb()