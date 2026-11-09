import math
#alpha-beta pruning function
def alpha_beta(depth,nodeindex,maximizingplayer,values,alpha,beta,height):
    #base case
    if depth==height:
        return values[nodeindex]
    if maximizingplayer:
        best=-math.inf

        for i in range(2):
            value=alpha_beta(
                depth + 1,
                nodeindex *2 + 1,
                False,
                values,
                alpha,
                beta,
                height
            )
            best=max(best,value)
            alpha=max(alpha,best)

            #beta cut off
            if beta<=alpha:
                break
        return best
    else:
        best=math.inf

        for i in range(2):
            value=alpha_beta(
                depth+1,
                nodeindex*2+1,
                True,
                values,
                alpha,
                beta,
                height
            )
            best=min(best,value)
            beta=min(beta,best)

            #alpha cut off
            if beta<=alpha:
                break
        return best
#main
values=list(map(int,input("enter 8 leaf node values: ").split()))
height=3
result=alpha_beta(
    0,
    0,
    True,
    values,
    -math.inf,
    math.inf,
    height
)
print("\noptimal value:",result)
