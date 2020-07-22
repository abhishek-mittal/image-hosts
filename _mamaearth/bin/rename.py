
# import os, re

# def main(): 

#     print('doing')
#     for count, filename in enumerate(os.listdir('./../assets copy')):
#         # dst = "a" + str(count) + '.png'
#         src = './../assets copy/' + filename
#         try:
#             key = '.' + filename.rsplit( ".", 1 )[1] 
#             print key
#         except Exception as identifier:
#             key = '.png'
        
#         dst = './../assets/' + re.sub('\s|\W', '', filename ) + key
#         # print filename.rsplit( ".", 1 )
#         os.rename(src, dst)

# if __name__ == '__main__':
#     main()