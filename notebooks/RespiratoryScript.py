import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
data = pd.read_csv(r'C:\Users\Natasha\Desktop\respiratory_disease_detection\datasets\Data_Entry_2017_v2020.csv')

#Previewing data
data.head()

data.rename(columns = {'Finding Labels': 'Respiratory_Disease'}, inplace=True)
data.head()

print('The Dataset contains ',data.shape[0],' rows and ',data.shape[1],' columns.')

data.drop(['Image Index', 'Follow-up #', 'OriginalImage[Width', 'Height]', 'OriginalImagePixelSpacing[x', 'y]'], axis=1, inplace=True)

data['Patient Age'].unique()

plt.plot()
sns.distplot(data['Patient Age'])
plt.title('Distribution of Patients Age')
plt.show()

data['Patient Gender'].value_counts()

data['Patient Gender'].value_counts().plot(kind='bar')
plt.title('Distribution of Respiratory Diseases by Gender')
plt.xlabel('Gender')
plt.ylabel('Frequency')
plt.show()

plt.plot()
sns.distplot(data['Respiratory_Disease'].value_counts())
plt.title('Distribution of Respiratory Diseases')
plt.show()

data = data.drop('Respiratory_Disease', axis=1).join(data['Respiratory_Disease'].str.split('|', expand=True).stack().reset_index(level=1, drop=True).rename('Respiratory_Disease'))
data.head()

data['Respiratory_Disease'].unique()

data.duplicated().any()
data.drop_duplicates()

data['Respiratory_Disease'].value_counts().plot(kind='bar')
plt.title('Distribution of Respiratory Diseases in the dataset')
plt.xlabel('Respiratory_Disease')
plt.ylabel('Frequency')
plt.show()

plt.plot()
sns.distplot(data['Respiratory_Disease'].value_counts())
plt.title('Distribution of Respiratory Diseases in the dataset')
plt.show()

sns.heatmap(data.corr(),annot=True)

app = dash.Dash()
app.layout = html.Div(children=[
    html.H1(children='Respiratory Disease Detection Dashboard'),
    dcc.Dropdown(id='Disease-dropdown',
                 options=[{'label': i, 'value': i}
                          for i in data['Respiratory_Disease'].unique()],
                 value='Cardiomegaly'),
    dcc.Graph(id='Disease-graph')
])
@app.callback(
    Output(component_id='Disease-graph', component_property='figure'),
    Input(component_id='Disease-dropdown', component_property='value')
)
def update_graph(selected_Disease):
    filtered_data = data[data['Respiratory_Disease'] == selected_Disease]
    bar_fig = px.bar(filtered_data,
                       x='Respiratory_Disease', y='Frequency',
                       color='type',
                       title=f'Distribution on {selected_Disease}')
    return bar_fig

if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)
