###########################
# lines.py
#
# class to automate getting
# and formatting lines
###########################
import feedparser

class Lines:
    def __init__(self, url='http://www.referincome.com/odds/rss2/football_nfl.xml'):
        self.d = feedparser.parse(url)

    def lines(self):
        ll = []
        l_double_names = ['New', 'Green', 'San', 'Tampa', 'Los']
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
            mando = str_title[-1]
            tup = (t1, spread, t2)
            ll.append(tup)
        return ll

    def print_for_fb(self):
        ll = self.lines()
        for l in ll:
            print l[0], l[1], '@', l[2]


if __name__ == "__main__":
    l = Lines()
    l.print_for_fb()