"""all-params script"""
import datapane as dp
import json

json_string = json.dumps(parameters, indent=2)

md = dp.Markdown(f"""
    # Script parameters
    You provided...
    ```
    {json_string}
    ```""")

def render():
    """Render and return your datapane report components"""
    return [dp.Markdown(md)]
