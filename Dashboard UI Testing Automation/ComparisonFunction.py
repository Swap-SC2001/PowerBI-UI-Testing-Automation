'''
Used to compare Title of both image extraction
'''
def Title_comparison(image1,image2):
    
    title1 = image1['title']
    title2 = image2['title']
    report = {"match":[],"not match":[],"exact match":""}
    try:
        img1 = title1.split()
        img2 = title2.split()
        for i in img1:
            if i in img2:
                report["match"].append(i)
            else:
                report["not match"].append({"image1":i})
        for j in img2:
            if j not in img1:
                report["not match"].append({"image2":j})
        if img1==img2:
            report["exact match"]="True"
            report["match"]=title1
        else:
            report["exact match"]="False"
        return report
    except:
        return None

    
'''
Used to compare Subtitle of both image extraction
'''
def SubTitle_comparison(image1,image2):
    
    title1 = image1['subtitle']
    title2 = image2['subtitle']
    report = {"match":[],"not match":[],"exact match":""}
    try:
        img1 = title1.split()
        img2 = title2.split()
        for i in img1:
            if i in img2:
                report["match"].append(i)
            else:
                report["not match"].append({"image1":i})
        for j in img2:
            if j not in img1:
                report["not match"].append({"image2":j})
        if img1==img2:
            report["exact match"]="True"
            report["match"]=title1
        else:
            report["exact match"]="False"

        return report
    except:
        return None 
'''
Used to compare color scheme
'''
def color_comparison(image1,image2):
    color1 = image1["color-scheme"]
    color2 = image2["color-scheme"]
    report = {"match":[],"not match":[]}
    for i in color1:
        if i in color2:
            report["match"].append(i)
        else:
            report["not match"].append({"Image 1":i})
    for i in color2:
        if i not in color1:
            report["not match"].append({"Image 2":i})
    return report
'''
Used to compare labels of both image extraction
'''
def label_comparison(image1,image2):

    legends1 = image1['legends']
    legends2 = image2['legends']
    report = {"match":[],"not match":{"image1":[],"image2":[]}}
    img1 = {}
    img2 = {}
    for i in legends1:
        img1[i["label"]]=i["color-scheme"]
    for i in legends2:
        img2[i["label"]]=i["color-scheme"]

    for i in img1.keys():
        if i in img2.keys():
            if img1[i] == img2[i]:
                report["match"].append({i:img1[i]})
            else:
                report["not match"]["image1"].append({i:img1[i]})
                report["not match"]["image2"].append({i:img2[i]})
                
        else:
            report["not match"]["image1"].append({"image1":{i:img1[i]}})
    for i in img2.keys():
        if i not in img1.keys():
            report["not match"]["image2"].append({"image2":{i:img2[i]}})
    return report
'''
Used to check axis labels and data distribution
'''
def X_axis_comparison(image1,image2):
    
    X_axis1_label = image1["X-axis"].get("label")
    X_axis2_label = image2["X-axis"].get("label")
    
    X_axis1_range = image1["X-axis"].get("range")
    X_axis2_range = image2["X-axis"].get("range")
    
    report = {"X-axis":{"label":{"match":[],"not match":[]},"range":{"match":[],"not match":[]}}}
    for i in X_axis1_range:
        if i in X_axis2_range:
            report["X-axis"]["range"]["match"].append(i)
        else:
            report["X-axis"]["range"]["not match"].append({"image1":i})
    for j in X_axis2_range:
        if j not in X_axis2_range:
            report["X-axis"]["range"]["not match"].append({"image2":j})
    if X_axis1_label==X_axis2_label:
        report["X-axis"]["label"]["match"].append(X_axis1_label)
    return report

def Y_axis_comparison(image1,image2):
    
    Y_axis1_label = image1["Y-axis"].get("label")
    Y_axis2_label = image2["Y-axis"].get("label")
    
    Y_axis1_range = image1["Y-axis"].get("range")
    Y_axis2_range = image2["Y-axis"].get("range")

    report = {"Y-axis":{"label":{"match":[],"not match":[]},"range":{"match":[],"not match":[]}}}
    for i in Y_axis1_range:
        if i in Y_axis2_range:
            report["Y-axis"]["range"]["match"].append(i)
        else:
            report["Y-axis"]["range"]["not match"].append({"image1":i})
    for j in Y_axis2_range:
        if j not in Y_axis2_range:
            report["Y-axis"]["range"]["not match"].append({"image2":j})
        if Y_axis1_label==Y_axis2_label:
            report["Y-axis"]["label"]["match"].append(Y_axis1_label)
    return report

'''
Used to compare table data
'''
def data_comparison(image1,image2):
    data1 = image1["data"]
    data2 = image2["data"]
    report = {"match":[],"not match":[]}
    for i in data1:
        for j in data2:
            if (i["column"]==j["column"] and i["row"]==j["row"]) or (i["column"]==j["row"] and i["row"]==j["column"]):
                if i["data"]==j["data"]:
                    report["match"].append(i)
                else:
                    report["not match"].append({"image1":i,"image2":j})
    return report   

def isStack(image1,image2):
    if image1["Stack"]==image2["Stack"]:
        return image1["Stack"]
    else:
        return {"image1":image1["Stack"],"image2":image2["Stack"]}

def line_type(image1,image2):
    if image1["line-type"]==image2["line-type"]:
        return image1["line-type"]
    else:
        return {"image1":image1["line-type"],"image2":image2["line-type"]}

'''
Used to compare segment of different segments
'''
def segment_comparison(image1,image2):

    segment1 = image1['segment']
    segment2 = image2['segment']
    report = {"match":[],"not match":{"image1":[],"image2":[]}}
    img1 = {}
    img2 = {}
    for i in segment1:
        img1[i["color-scheme"]]=i["value"]
    for i in segment2:
        img2[i["color-scheme"]]=i["value"]

    for i in img1.keys():
        if i in img2.keys():
            if img1[i] == img2[i]:
                report["match"].append({i:img1[i]})
            else:
                report["not match"]["image1"].append({i:img1[i]})
                report["not match"]["image2"].append({i:img2[i]})
        else:
            report["not match"]["image1"].append({i:img1[i]})
    for i in img2.keys():
        if i not in img1.keys():
            report["not match"]["image2"].append({i:img2[i]})          
    return report     

def value_label_comparison(image1,image2):
    data1=image1['data']
    data2=image2['data']
    img1 = {}
    img2 = {}
    report = {"match":[],"not match":{"image1":[],"image2":[]}}
    for i in data1:
        img1[i["label"]]=i["value"]
    for i in data2:
        img2[i["label"]]=i["value"]
    for i in img1.keys():
        if i in img2.keys():
            if img1[i] == img2[i]:
                report["match"].append({i:img1[i]})
            else:
                report["not match"]["image1"].append({i:img1[i]})
                report["not match"]["image2"].append({i:img2[i]})
        else:
            report["not match"]["image1"].append({i:img1[i]})
    for i in img2.keys():
        if i not in img1.keys():
            report["not match"]["image2"].append({i:img2[i]})          
    return report

def value_label_color_comparison(image1,image2):
    data1=image1['data']
    data2=image2['data']
    img1c={}
    img2c={}
    img1v={}
    img2v={}
    for i in data1:
        img1v[i["label"]]=i["value"]
    for i in data2:
        img2v[i["label"]]=i["value"]
    for i in data1:
        img1c[i["label"]]=i["color"]
    for i in data2:
        img2c[i["label"]]=i["color"]
    report = {"match":{"color":[],"value":[]},"not match":{"color":{"image1":[],"image2":[]},"value":{"image1":[],"image2":[]}}}
    for i in img1c.keys():
        if i in img2c.keys():
            if img1c[i] == img2c[i]:
                report["match"]["color"].append({i:img1c[i]})
            else:
                report["not match"]["color"]["image1"].append({i:img1c[i]})
                report["not match"]["color"]["image2"].append({i:img2c[i]})
        else:
            report["not match"]["color"]["image1"].append({i:img1c[i]})
    for i in img2c.keys():
        if i not in img1c.keys():
            report["not match"]["color"]["image2"].append({i:img2c[i]})
    
    
    for i in img1v.keys():
        if i in img2v.keys():
            if img1v[i] == img2v[i]:
                report["match"]["value"].append({i:img1v[i]})
            else:
                report["not match"]["value"]["image1"].append({i:img1v[i]})
                report["not match"]["value"]["image2"].append({i:img2v[i]})
        else:
            report["not match"]["value"]["image1"].append({i:img1v[i]})
    for i in img2v.keys():
        if i not in img1v.keys():
            report["not match"]["value"]["image2"].append({i:img2v[i]})
    return report

def min_max_value(image1,image2):
    data1=image1['data']
    data2=image2['data']
    report = {"match":[],"not match":{"image1":[],"image2":[]}}
    for i in data1:
        if i in data2:
            report["match"].append(i)
        else:
            report["not match"]["image1"].append(i)
    for j in data2:
        if j not in data1:
            report["not match"]["image2"].append(j)
    return report

def card_multi(image1,image2):
    value1=image1['value']
    value2=image2['value']
    report = {"match":[],"not match":{"image1":[],"image2":[]}}
    for i in value1:
        if i in value2:
            report["match"].append(i)
        else:
            report["not match"]["image1"].append(i)
    for j in value2:
        if j not in value1:
            report["not match"]["image2"].append(j)
    return report

def card_single(image1,image2):
    value1=image1['value']
    value2=image2['value']
    report = {"match":[],"not match":{"image1":[],"image2":[]}}
    if value1==value2:
        report["match"].append(value1)
    else:
        report["not match"]["image1"].append(value1)
        report["not match"]["image2"].append(value2)
    return report

def chart_type(image1,image2):
    chart1  = image1['chart-type']
    chart2  = image2['chart-type']
    report = {"match":[],"not match":{}}
    if chart1==chart2:
        report['match'].append(chart1)
    else:
        report['not match']['image1'] = chart1
        report['not match']['image2'] = chart2
    return report
def heirarchy(image1,image2):
    heirarchy1 = image1['heirarchy']
    heirarchy2 = image2['heirarchy']
    report = {"match":{},"not match":{"image1":{},"image2":{}}}
    img1_h = {}
    img2_h = {}
    for i in heirarchy1:
        if i["level"] not in img1_h.keys():
            img1_h[i["level"]]=[{"label":i["label"],"value":i["value"]}]
        else:
            img1_h[i["level"]].append({"label":i["label"],"value":i["value"]})
    for i in heirarchy2:
        if i["level"] not in img2_h.keys():
            img2_h[i["level"]]=[{"label":i["label"],"value":i["value"]}]
        else:
            img2_h[i["level"]].append({"label":i["label"],"value":i["value"]})
    for i in img1_h:
        for j in img2_h:
            if i==j:
                for k in img1_h[i]:
                    if k in img2_h[j]:
                        if k not in report["match"].keys():
                            report["match"][i]=k
                        else:
                            report["match"][i].append(k)
                    else:
                        if k not in report["not match"]["image1"].keys():
                            report["not match"]["image1"][i]=k
                        else:
                            report["not match"]["image1"][i].append(k)
                break
    for i in img2_h:
        for j in img1_h:
            if i==j:
                for k in img2_h[i]:
                    if k not in img1_h[j]:
                        if k not in report["not match"]["image2"].keys():
                            report["not match"]["image2"][i]=k
                        else:
                            report["not match"]["image2"][i].append(k)
                break
    return report

def stats(image1,image2):
    data1=image1['stats']
    data2=image2['stats']
    img1 = {}
    img2 = {}
    report = {"match":[],"not match":{"image1":[],"image2":[]}}
    for i in data1:
        img1[i["label"]]=i["value"]
    for i in data2:
        img2[i["label"]]=i["value"]
    for i in img1.keys():
        if i in img2.keys():
            if img1[i] == img2[i]:
                report["match"].append({i:img1[i]})
            else:
                report["not match"]["image1"].append({i:img1[i]})
                report["not match"]["image2"].append({i:img2[i]})
                
        else:
            report["not match"]["image1"].append({"image1":{i:img1[i]}})
    for i in img2.keys():
        if i not in img1.keys():
            report["not match"]["image2"].append({"image2":{i:img2[i]}})
    return report


def start(image1,image2):
    start1 = image1['start']
    start2 = image2['start']
    report = {"match":[],"not match":{}}
    if start1 == start2:
        report["match"].append(start1)
    else:
        report["not match"]["image1"]=start1
        report["not match"]["image2"]=start2
    return report

def end(image1,image2):
    end1 = image1['end']
    end2 = image2['end']
    report = {"match":[],"not match":{}}
    if end1 == end2:
        report["match"].append(end1)
    else:
        report["not match"]["image1"]=end1
        report["not match"]["image2"]=end2
    return report


        
