def solution(total_lambs):
    # Your code here

    def stingy(total_lambs):
        n,total = 0,1
        count = 0
        while (total_lambs >0):
            n,total = total,total+n
            count+=1
            total_lambs -= total

        return count

    def gen(total_lambs):
        i=1
        count = 0
        while total_lambs > 0:
            i *= 2
            total_lambs -= i
            count +=1
        return count

    return (stingy(total_lambs)-gen(total_lambs))
