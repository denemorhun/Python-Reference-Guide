# EASY
'''
calculate_max_hourglass. Since we have padded values with 0, we don't need to implement an if statement. 

'''

def calculate_max_hourglass(input) -> bool:

    arr = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0],[0, 0, 2, 4, 4, 0],[0, 0, 0, 2, 0, 0],
[0, 0, 1, 2, 4, 0]]
        
    mysum = []
    
    for i in range(4):
        for j in range(4):
            result = sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3])
            mysum.append(result)
                
    print(max(mysum))
           

if __name__ == '__main__':
        input = ""

        result = count_hg(input)

        print("Yes" if result else "No")