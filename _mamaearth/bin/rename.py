
import os, re, random, string
def generate_id(size=7, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))


def main(): 

    print('doing')

    for count, filename in enumerate(os.listdir( './assets')):
        # dst = "a" + str(count) + '.png'
        src = './assets/' + filename
        # print(count)
        try:
            key = '.' + filename.rsplit( ".", 1 )[1]
        except Exception as identifier:
            key = '.png'
        
        c = re.findall('\s+', filename)
        tt = bool(len(c))

        if tt:
            print(tt)
            dst = './assets/' + re.sub('\s|\W', '', filename ) + generate_id() + key
            print dst
            os.rename(src, dst)


if __name__ == '__main__':
    main()