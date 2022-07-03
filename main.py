import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門') #タイトル作成



st.write('DataFrame') #テキストの追加

df = pd.DataFrame({
    '1列目' : [1, 2, 3, 4],
    '2列目' : [10, 20, 30, 40]
}) #データフレーム(表)の作成

 #動的な表の表示　表の大きさ(px単位)指定可能 列の最大値を色付け
st.dataframe(df.style.highlight_max(axis = 0), width = 100, height = 100)

#静的な表の表示 ソート等ができない
st.table(df)

#表の作り方調べstreamlit -> docs -> referenceguide -> api reference -> display data

#マジックコマンド
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

#折れ線グラフ
oresen = pd.DataFrame(
    np.random.rand(20, 3),#20行3列ランダムな数表示
    columns = ['a', 'b', 'c']
)

st.line_chart(oresen)

#マッププロット
map = pd.DataFrame(
    np.random.rand(100, 2)/[50,50] + [35.69, 139.70],#新宿周辺の緯度経度をランダムに表示
    columns = ['lat', 'lon'] # 緯度経度
)

st.map(map)

#画像表示
st.write('Display Image')
#チェックボックス(画像表示するか否か)
if st.checkbox('Show Image'):
    img = Image.open('IMG_8603.jpg')
    st.image(img, caption = 'Kohsuke Horie', use_column_width = True)

#セレクトボックス
st.write('Interactive Widgets')
option = st.selectbox(
    'あなたが好きな数字を教えてください',
    list(range(1,11))
    )

'あなたの好きな数字は、', option, 'です'
#sidebarの追加
#st.sidebar.~

#2カラムレイアウト
left_column, right_column = st.columns(2)
button = left_column.button(' 右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

text = st.text_input('あなたの趣味は何ですか')
'あなたの趣味:', text

condition = st.slider('How are you?', 0, 100, 50)
'condition:', condition

#expander
expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')

#プログレスバー
st.write('プログレスバーの表示')
'Start'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)
'Done'
