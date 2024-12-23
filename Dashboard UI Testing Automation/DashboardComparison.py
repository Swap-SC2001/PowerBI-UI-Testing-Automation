# all required libraries are here
import streamlit as st
from streamlit_javascript import st_javascript
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
import PIL
import json
import ComparisonFunction
import re
import pandas as pd


#read JSON prompts
knowledge_db = open('DashboardComparison_Knowledge.json')
prompts = json.load(knowledge_db)
# streamlit headings
st.set_page_config(page_title="Dashboard Comparison", page_icon="💹", layout="wide")
st.header("Dashboard Comparison")

# clear the session state
def clear_submit():
    st.session_state["submit"] = True
    st.session_state.temp=st.session_state.temp+0.00001

# image uploading function 
def displayimage(upl_file, width):
    st.image(upl_file, caption='Uploaded Image',width=width)
 

def print_Comparison(result1_json,result2_json,diagram_type):
    comparison_dict = {}

    Mapping = {
    "default":{
        "title":ComparisonFunction.Title_comparison,
        "subtitle":ComparisonFunction.SubTitle_comparison,
        "color-scheme":ComparisonFunction.color_comparison,
        "legends":ComparisonFunction.label_comparison
    },
    "Barchart-Horizontal":{
        "X-axis":ComparisonFunction.X_axis_comparison,
        "Y-axis":ComparisonFunction.Y_axis_comparison,
        "Stack":ComparisonFunction.isStack,
        "data":ComparisonFunction.value_label_comparison
    },
    "Barchart-Vertical":{
        "X-axis":ComparisonFunction.X_axis_comparison,
        "Y-axis":ComparisonFunction.Y_axis_comparison,
        "Stack":ComparisonFunction.isStack,
        "data":ComparisonFunction.value_label_comparison
    },
    "Line-Chart":{
        "line-type":ComparisonFunction.line_type
    },
    "Barchart-Linechart":{
        "X-axis":ComparisonFunction.X_axis_comparison,
        "Y-axis":ComparisonFunction.Y_axis_comparison,
        "Stack":ComparisonFunction.isStack,
        "data":ComparisonFunction.data_comparison,
        "line-type":ComparisonFunction.line_type
    },
    "Columnchart-Linechart":{
        "X-axis":ComparisonFunction.X_axis_comparison,
        "Y-axis":ComparisonFunction.Y_axis_comparison,
        "Stack":ComparisonFunction.isStack,
        "data":ComparisonFunction.data_comparison,
        "line-type":ComparisonFunction.line_type
    },
    "Doughnut-Chart":{
        "segment":ComparisonFunction.segment_comparison,
    },
    "Funnel-Chart":{
        "data":ComparisonFunction.value_label_color_comparison
    },
    "Gauge-Chart":{
        "data":ComparisonFunction.min_max_value
    },
    "Card-Multirow":{
        "label":ComparisonFunction.label_comparison,
        "value":ComparisonFunction.card_multi
    },
    "Card-SingleNumber":{
        "label":ComparisonFunction.label_comparison,
        "value":ComparisonFunction.card_single
    },
    "Heat-Map":{
        "data":ComparisonFunction.value_label_color_comparison
    },
    "Point-Map":{
        "data":ComparisonFunction.value_label_color_comparison
    },
    "Matrix":{
        "data":ComparisonFunction.data_comparison
    },
    "Pie-Chart":{
        "segment":ComparisonFunction.segment_comparison
    },
    "Scatter":{
        "X-axis":ComparisonFunction.X_axis_comparison,
        "Y-axis":ComparisonFunction.Y_axis_comparison,
        "line":ComparisonFunction.line_type
    },
    "Slicer":{
        "chart-type":ComparisonFunction.chart_type
    },
    "Table":{
        "data":ComparisonFunction.data_comparison
    },
    "Tree-Map":{
        "segment":ComparisonFunction.segment_comparison,
        "heirarchy":ComparisonFunction.heirarchy,
        "stats":ComparisonFunction.stats
    },
    "Waterfall-Chart":{
        "start":ComparisonFunction.start,
        "end":ComparisonFunction.end
    }

    }
    comparison_dict = {}
    default = Mapping["default"]
    for i in default.keys():
        if i in result1_json.keys() and i in result2_json.keys() :
            comparison_dict[i]=Mapping["default"][i](result1_json,result2_json)
    diagram = Mapping[diagram_type]
    for i in diagram.keys():
        if i in result1_json.keys() and i in result2_json.keys():
            comparison_dict[i]=Mapping[diagram_type][i](result1_json,result2_json)
    return comparison_dict

def JSON_searcher(strings):
    Str_dict = re.findall(r'\{.*\}',strings)
    try:
        return Str_dict
    except:
        st.error("Failed to extract")
        return Str_dict


def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out


def image1(systemprompt,prompt_default,prompt,model_name,GOOGLE_API_KEY,temp,tokens,image_url1):
    #main llm defination
    llm = ChatGoogleGenerativeAI(model=model_name,google_api_key=GOOGLE_API_KEY,
                                temperature=temp,maxOutputTokens=tokens,
                                top_k=20,top_p=0.5,)

    input2 = HumanMessage(
        content=[
            {"type": "text",
            "text": systemprompt},
            {"type": "text",
            "text": prompt_default},
            {"type": "text",
            "text": prompt},
            {"type": "image_url", "image_url": image_url1},
        ]
    )
    result = llm.invoke([input2])
    result=result.content
    return result


def image2(systemprompt,prompt_default,prompt,model_name,GOOGLE_API_KEY,temp,tokens,image_url2):
    #main llm defination
    llm = ChatGoogleGenerativeAI(model=model_name,google_api_key=GOOGLE_API_KEY,
                                temperature=temp,maxOutputTokens=tokens,
                                top_k=20,top_p=0.5,)  
    
    input2 = HumanMessage(
        content=[
            {"type": "text",
            "text": systemprompt},
            {"type": "text",
            "text": prompt_default},
            {"type": "text",
            "text": prompt},
            {"type": "image_url", "image_url": image_url2},
        ]
    )
    result = llm.invoke([input2])
    result=result.content
    return result


# upload image, give api-key, ui elements neo4j credentials
if 'submit' not in st.session_state:
    st.session_state.submit=False
with st.sidebar:
    model_name = st.radio("Select the model", ("gemini-1.5-flash-001",) , key = 'model')
    GOOGLE_API_KEY = st.text_input("API Key", key="api_key", type='password')   

    diagram_type = st.selectbox("Select the diagram type", ('Barchart-Horizontal', 'Barchart-Vertical', 'Line-Chart', 'Barchart-Linechart', 'Columnchart-Linechart', 'Doughnut-Chart', 'Funnel-Chart', 'Gauge-Chart', 'Card-Multirow', 'Card-SingleNumber', 'Heat-Map', 'Point-Map', 'Matrix', 'Pie-Chart', 'Scatter', 'Slicer', 'Table', 'Tree-Map', 'Waterfall-Chart'), key = 'diagram')
    
    # sliders for custom parameters
    temp = st.slider('Temperature', 0.0, 1.0, 0.0,key='temp')
    st.write("Selected temperature:  ", temp, ' .')
    tokens = st.slider('max output tokens', 0, 4000, 3200)
    st.write("Selected max tokens:  ", tokens, ' .')  
    
    uploaded_file1 = st.file_uploader(
        "Upload file 1",
        type=['png'],
        help="Only png files are supported",
        on_change=clear_submit,)
    # display the image uploaded
    if uploaded_file1:
        ui_width = st_javascript("window.innerWidth" , key = 'image1')
        displayimage(uploaded_file1, ui_width+10)
        # creating a image reader object
        image_url1 = PIL.Image.open(uploaded_file1)

    

    uploaded_file2 = st.file_uploader(
        "Upload file 2",
        type=['png'],
        help="Only png files are supported",
        on_change=clear_submit,)
    # display the image uploaded
    if uploaded_file2:
        ui_width = st_javascript("window.innerWidth" , key = 'image2')
        displayimage(uploaded_file2, ui_width+10)
        # creating a image reader object
        image_url2 = PIL.Image.open(uploaded_file2)


def print_df(result1_out,result2_out,comparison):
    st.write("Image 1 analysis:\n-------------------------\n")
    st.dataframe(pd.DataFrame([flatten_json(result1_out)]))
    st.write("Image 2 analysis:\n-------------------------\n")
    st.dataframe(pd.DataFrame([flatten_json(result2_out)]))
    st.write("Comparison:\n-------------------------\n")
    st.dataframe(pd.DataFrame([flatten_json(comparison)]))

def print_JSON(result1_out,result2_out,comparison):
    st.write("Image 1 analysis:\n-------------------------\n",result1_out)
    st.write("Image 2 analysis:\n-------------------------\n",result2_out)
    st.write("Comparison:\n-------------------------\n",comparison)




if model_name and diagram_type and GOOGLE_API_KEY and uploaded_file1 and image_url1 and uploaded_file2 and image_url2:


    #define the load button for the main model
    load = st.button('Load Model')

    
    # for stacked bottons used session_state
    if "load_state" not in st.session_state:
        st.session_state.load_state = False

    if load or st.session_state.load_state:
            st.session_state.load_state = True

    
            systemprompt = json.dumps(prompts["prompt"])
            prompt_default = json.dumps(prompts["default"])
            prompt1=json.dumps(prompts[diagram_type])

            result1=image1(systemprompt,prompt_default,prompt1,model_name,GOOGLE_API_KEY,temp,tokens,image_url1)
            result1_str = JSON_searcher(result1)
            
            result2=image2(systemprompt,prompt_default,prompt1,model_name,GOOGLE_API_KEY,temp,tokens,image_url2)
            result2_str = JSON_searcher(result2)
            comparison = {}
            result1_out = {}
            result2_out = {}
            for i in result1_str:
                for j in result2_str:
                    try:
                        result1_json = json.loads(i)
                    except:
                        break
                    try:
                        result2_json = json.loads(j)
                    except:
                        break
                    comparison_dict = print_Comparison(result1_json,result2_json,diagram_type)
                    for x in result1_json.keys():
                        result1_out[x]=result1_json[x]
                    for y in result2_json.keys():
                        result2_out[y]=result2_json[y]
                    for k in comparison_dict.keys():
                        comparison[k]=comparison_dict[k]
            JSON_Format = st.button("JSON",key="printJSON")
            Table_Format = st.button("Table",key="printTable")
            if JSON_Format:
                print_JSON(result1_out,result2_out,comparison)
                Table_Format = False
            if Table_Format:
                print_df(result1_out,result2_out,comparison)
                JSON_Format = False
        

else:
    st.write(" PLEASE ENTER ALL THE DETAILS IN THE SIDEBAR ")

