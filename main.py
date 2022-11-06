import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title("Streamlit 超入門")

st.write("DataFrame")

df = pd.DataFrame({
    "1列目":[1,2,3,4],
    "2列目":[10,20,30,40]
})

#st.table(df.style.highlight_max(axis=0))

"""
# 章
## 節
### 項
```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""

df = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c']
)
st.bar_chart(df)


df = pd.DataFrame(
    np.random.rand(100,2)/[50,50]+[35.69,139.70],
    columns=['lat','lon']
)
st.map(df)

# st.write("Display Image")

# option = st.selectbox(
#     "あなたが好きな数字を教えてください！",
#     list(range(1,11))
# )
# "あなたの好きな数字は、",option,"です。"

# if st.checkbox("Show Image"):
#     img=Image.open("hobby_moto1.jpg")
#     st.image(img, caption="Suzuki GSR250", use_column_width=True)

# st.write("インタラクティブなウィジェット")
# text = st.text_input("あなたの趣味を教えてください。")
# "あなたの趣味は、",text,"です。"

# st.sidebar.write("サイドバー")
# text = st.sidebar.text_input("あなたの趣味を教えてください。")
# condition = st.sidebar.slider("あなたの今の調子は？",0,100,50)
# "あなたの趣味は、",text,"です。"
# "コンディション：",condition

st.write("見た目を整える方法")
left_columun, right_column = st.columns(2)
button = left_columun.button("右カラムに文字を表示")
if button:
    right_column.write("ここは右カラムですyo")


inquire = st.expander("問合せ")
inquire.write("問合せ内容を書く")
inquire.write("あいうえお")

st.write("プログレスバーの表示")
"Start!!!"
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)
"Done!!!"


