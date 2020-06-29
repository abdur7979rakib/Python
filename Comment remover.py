code=''' int x=10;// Hi
    /* hi How are you */
    int 2; // comment
'''
count = 0
def remove_comment(content):
    index = 0
    comment_line_inside = False
    comment_block_level = 0
    result = []
    while index < len(content):
        if content[index] == '/' and index + 1 < len(content) and content[index+1] == '*':
            comment_block_level += 1
        elif content[index] == '/' and content[index-1] == '*':
            comment_block_level -= 1
        elif content[index] == '/' and index + 1 < len(content) and content[index + 1] == '/':
            comment_line_inside = True
        elif content[index] == '\n' and comment_line_inside == True:
            comment_line_inside = False
        elif not comment_line_inside and comment_block_level == 0:
            result.append(content[index])
        index += 1

    return ''.join(result)


if __name__ == "__main__":
    print (remove_comment(code))

