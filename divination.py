import streamlit as st
st.title("欢迎来到'网络占卜师'")
name=st.text_input("请输入名字:")
age=st.text_input("请输入年龄:")
birth=st.text_input("请输入生日:")
star=st.text_input("请输入星座:")
if st.button("结果"):
    st.write(
f"""{name},年龄{age},星座{star}
将在下个星期有点小幸运 
在学业上 只要努力必有好结果 
如有考试 考卷上的全是读过的 非常了解的 
如有organic chemistry 一定只出alkane和alkene
如有biology 必出你最了解的身体部位（不会有骨头）
ʕᵔᵜᵔʔ""")
