from tkinter import *

#Sample chemical reactions

flowchart = {}

flowchart['Alkanes'] = {}
flowchart['Alkanes']['Alcohols'] = 'Controlled Oxidation (Cu,523K,100atm)|(KMn04)'
flowchart['Alkanes']['Alkanal'] = 'Controlled Oxidation (Mo203, heat)'
flowchart['Alkanes']['Carboxylic Acids'] = 'Controlled Oxidation ((CH3C00)2Mn,heat)'
flowchart['Alkanes']['Alkyl Halides'] = 'Halogentation,returns even # chain'
flowchart['Alkanes']['Benzene'] = 'Cr203/V205/Mo203,773K,10-20atm'

flowchart['Alcohols'] = {} 
flowchart['Alcohols']['Alkenes'] = 'Acidic Dehydration (H2SO4)'

flowchart['Alkenes'] = {}
flowchart['Alkenes']['Alkanes'] = 'Hydrogenation'
flowchart['Alkenes']['Alcohols'] = '(H2O)'
flowchart['Alkenes']['Vicinal Dihalides'] = 'Halogenation' 
flowchart['Alkenes']['Vicinal Glycols'] = 'Cold dil. KMnO4 ("Baeyer\'s Reagent")'
flowchart['Alkenes']['Carboxylic Acids'] = 'KMnO4/H+'
flowchart['Alkenes']['Ketones'] = 'KMnO4/H+'
flowchart['Alkenes']['Polymers'] = 'KMnO4/H+ (catalyst, increase heat'

flowchart['Vicinal Dihalides'] = {}
flowchart['Vicinal Dihalides']['Alkenes'] = 'Dehalogenation'
flowchart['Vicinal Dihalides']['Alkenyl Halides'] = '+alc. KOH'

flowchart['Alkyl Halides'] = {}
flowchart['Alkyl Halides']['Alkanes'] = 'Zn/H+' 
flowchart['Alkyl Halides']['Alkenes'] = 'Dehydrohalogenation (beta-elimination reaction) (alc. KOH, heat)'

flowchart['Carboxylic Acids'] = {}
flowchart['Carboxylic Acids']['Alkanes'] = 'Decarboxylation (NaOH/CaO)'

flowchart['Alkenyl Halides'] = {}
flowchart['Alkenyl Halides']['Alkynes'] = 'Sodamide NaNH2'

flowchart['Alkynes'] = {}
flowchart['Alkynes']['Vicinal Dihalides'] = 'Zinc'
flowchart['Alkynes']['Benzene'] = 'Red hot iron tube, 873K'
flowchart['Alkynes']['Polymers'] = 'Polyacetylene'
flowchart['Alkynes']['cis-Alkenes'] = 'Partial Reduction, ("Paladised charcoal"-Lindlar\'s catalyst)'
flowchart['Alkynes']['trans-Alkenes'] = 'Na, liq. NH3'

flowchart['Alkanal'] = {}
flowchart['Ketones'] = {}
flowchart['Polymers'] = {}
flowchart['Benzene'] = {}
flowchart['Vicinal Glycols'] = {}
flowchart['cis-Alkenes'] = {}
flowchart['trans-Alkenes'] = {}
flowchart['Carboxylic Acids'] = {}

def dijkstra(graph, start, end):
    optimalDist = {}
    predecessor = {}
    unseenNodes = {key:flowchart[key] for key in flowchart}
    infinity = float('inf')
    path = []
    outputs = []

    for node in unseenNodes:
        optimalDist[node] = infinity
    optimalDist[start] = 0
    while unseenNodes:
        min_distance_node = None
        for node in unseenNodes:
            if min_distance_node == None:
                min_distance_node = node
            elif optimalDist[node] < optimalDist[min_distance_node]:
                min_distance_node = node
        path_options = graph[min_distance_node].items()

        for child_node,reaction in path_options:
            if 1 + optimalDist[min_distance_node] < optimalDist[child_node]:
                optimalDist[child_node] = 1 + optimalDist[min_distance_node]
                predecessor[child_node] = min_distance_node
        unseenNodes.pop(min_distance_node)

    currentNode = end

    while currentNode != start:
        try:
            path.insert(0,currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            outputs.append('Path not reachable')
            return outputs
    path.insert(0,start)

    if optimalDist[end] != infinity:
        outputs.append("Steps in reaction is: " + str(optimalDist[end]))
        outputs.append(path)
        
        for i in range(len(path)):
            if i == (len(path)-1):
                break
            else:
                reactant = path[i]
                product = path[i+1]
                reaction = reactant + " to " + product + " is done by " + flowchart[reactant][product]
                outputs.append(reaction)
        return outputs


# start = input("Enter type of organic compund that will be reacted: ")
# end = input("Enter type of organic compund that needs to be produced: ") 
# outputs = dijkstra(flowchart,start,end)

''' outputs values
    0-Path not reachable
      Steps in reaction is: ___
    1-Path list
    2-flowchart[reactant][product]
'''

root = Tk()
root.title('Organic Chemistry Reactions Converter')
root.geometry("604x300")
root.configure(background='#2ab7ca')

dropdownItems = list(flowchart.keys())

dropbg = "#fed766"
dropfg = "#FFFFFF"
buttonsbg = "#F4B345"
buttonsfg = "#363636"

reactantClicked = StringVar()
reactantClicked.set(dropdownItems[0])
dropReactant = OptionMenu(root, reactantClicked, *dropdownItems).place(x=4,y=4, height=40, width=300)

productClicked = StringVar()
productClicked.set(dropdownItems[0])
dropProduct = OptionMenu(root, productClicked, *dropdownItems).place(x=304,y=4, height=40, width=300)

def reactions():
    start = reactantClicked.get()
    end = productClicked.get()

    outputs = dijkstra(flowchart,start,end)

    if len(outputs) > 1:
        steps, path, *reactions = outputs
    else:
        myLabel = Label(root,text='Path Not Reachable', bg="#ff8c1a").place(x=4,y=92, height=20, width=600)
        return False
    
    StepsLabel = Label(root, text=steps, bg="#b3cde0").place(x=4,y=92, height=20, width=600)
    PathLabel = Label(root, text="Path taken "+str(path), bg="#b3cde0").place(x=4,y=116, height=20, width=600)
    for i in range(len(reactions)):
        ReactionLabel = Label(root, text=reactions[i], bg="#6497b1").place(x=4,y=(140+i*24), height=20, width=600)

def clear():
    clearLabel = Label(root, text="", bg="#2ab7ca").place(x=4,y=92, height=300, width=600)
    return

reactionsButton = Button(root, text = 'Convert', command=reactions, bg="#011f4b", fg="#ffffff").place(x=4,y=44, height=20, width=600)
clearButton = Button(root, text = 'Clear', command=clear, bg="#011f4b", fg="#ffffff").place(x=4,y=68, height=20, width=600)

root.mainloop()