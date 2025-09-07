# Model Context Protocol - Implementation



## 1) Emoji Usage MCP
### Dataset
This project uses the [🌟 Emoji Trends Dataset ](https://www.kaggle.com/datasets/waqi786/emoji-trends-dataset) provided by Kaggle.
Its main intent is to provide information about the usage of emojis via mcp tools to an LLM applying the correct queries to the dataset. Among the different tools provided, you can find the following in two distinct categories for usage: 

**a) Checking Validity**
| Tool | Desrciption ||
|---|---|---|
| `get_describers` | Tool to detect valid describers for emoji usaged. To avoid restrictions on query excecutions and  |
| `get_possible_contexts` | Returns the feeling/context category from the datset so that the LLM can parse it into natural language |
| `get_possible_platforms` | Gives a list of plaftorms which usage can be tracked down via the dataset |
| `is_valid_emoji` | Detects if the current dataset contains informatio about the emoji in question to assure the validity of the responses/queries |
|

**b) Interpreting Emoji Usage**
| Tool | Desrciption ||
|---|---|---|
| `get_context_from_emoji` | Tool to detect valid describers for emoji usaged. To avoid restrictions on query excecutions and  |
| `get_platform_from_emoji` | Returns the feeling/context category from the datset so that the LLM can parse it into natural language |
| `get_gender_from_emoji` | Gives a list of plaftorms which usage can be tracked down via the dataset |
|

**c) Predicting Emoji Usage**
| Tool | Desrciption ||
|---|---|---|
| `get_appropriate_emoji` | Returns one or more emojis suitable for the given situation or list of conditions, ordered by how frequently it appears in the dataset for Emoji Usage  | 
|
## Dependencies
For the mcp protocol itself `uv` is used as the package manager for this project with `mcp` and `mcp[cli]` for the actual protocol, using the official sdk for python. Also, for enforcing structure in the tools `pydantic` is used, and `pandas` for the queries.

## Scripts
### Setup
```
cd emoji-use-mcp
uv run mcp
```
### Dev
  ```
  cd emoji-use-mcp
  uv mcp dev server.py
  ```
### Run

```
  cd emoji-use-mcp
  uv run mcp install server.py
  uv mcp dev server.py
```
## References
The official repository for mcp with python and the developer kit helped a lot
```
https://github.com/modelcontextprotocol/python-sdk?tab=readme-ov-file#adding-mcp-to-your-python-project
```