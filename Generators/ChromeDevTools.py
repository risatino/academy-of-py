# jupyter notebook allows you to open a dev tool called Chrome-view-developer-developerTools
from IPython.core.display import HTML

# jupyter notebook has a function that gives you access to the DOM
HTML('''
<h1>Hello DOM!</h1>
''')

# Now you can add a style class
HTML('''
<style scoped>
.steelbleu {
    color: steelblue;
    font: 25px;
} 
</style>
<h3 class="steelbleu">Sup DOM!</h3>
''')
