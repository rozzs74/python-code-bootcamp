# https://www.hackerrank.com/challenges/designer-pdf-viewer/problem

def designerPdfViewer(h, word):
    maxHeight=0
    for i in range(len(word)):
        if(h[ord(word[i])-97] > maxHeight):
            maxHeight=h[ord(word[i])-97]
    return len(word)*1*maxHeight

a = designerPdfViewer([1 ,3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5,5, 5, 5, 5, 5, 5,5, 5, 5, 5, 5, 5], "abc")
print(a)