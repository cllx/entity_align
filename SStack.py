# python栈的实现
class SStack():          #基于顺序表技术实现的栈类
    def __init__(self):  #用list对象_elems存储栈中元素
        self._elems=[]   #所有栈操作都映射到list操作
    def is_empty(self):
        return self._elems==[]
    def top(self):      #取得栈顶元素，不删除
        if self.is_empty():
            print('为空栈!')
            return
        return self._elems[-1]
    def push(self,elem):      #将元素压入栈
        self._elems.append(elem)
    def pop(self):           #将栈顶元素弹出
        if self.is_empty():
            print('为空栈!')
            return
        return self._elems.pop()

if __name__ == '__main__':
    st = SStack()
    for i in range(1,10,2):
        st.push(i)
    while not st.is_empty():
       print("   ",st.pop())