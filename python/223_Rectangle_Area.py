class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        width,hight = 0,0
        if E < C and B < H:
            width = max(0 , min(C,G) - max(A,E))
            hight = max(0 , min(D,H) - max(B,F))
            return (C-A)*(D-B) + (G-E)*(H-F) - width * hight
        else:
            return (C-A)*(D-B) + (G-E)*(H-F)
