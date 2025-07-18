import re

def parse_mixed_lines(multiline_string, n):
    items = []

    for line in multiline_string.strip().splitlines():
        line = line.strip()
        if not line:
            continue
        
        numbers = re.findall(r"\b\d+\b", line)
        text_only = re.sub(r"\b\d+\b", "", line).strip()

        if text_only:
            items.append(text_only)
        items.extend(numbers)

    chunks = [items[i:i + n] for i in range(0, len(items), n)]
    return chunks

multiline_str = """

"""

n = 13
result = parse_mixed_lines(multiline_str, n)
for chunk in result:
    print(chunk)
import pandas as pd
df = pd.DataFrame(result, columns=['Sr No.','Form No.','Student Name','Batch','Campus','Test Rank','CAMPUS RANK','BATCH RANK','300','%','Phy','Chem','Math'])
modi_df=df[df['Batch']=='P4TE_1A_AA0'][['Student Name','300','Phy','Chem','Math']].sort_values(by='Student Name')
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
print(modi_df)
modi_df.to_excel(".xlsx",index=False)
