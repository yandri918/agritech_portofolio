import re
import os

filepath = r"c:\Users\yandr\OneDrive\Desktop\agrisensa-api\agrisensa_commodities\services\jamu_calculator_service.py"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Let's extract water and result from "preparation" string and add them as explicit keys in the dict
def replacer(match):
    full_str = match.group(0)
    # find preparation string
    prep_match = re.search(r'"preparation": "(.*?)"', full_str)
    if prep_match:
        prep_str = prep_match.group(1)
        w_match = re.search(r'(\d+)\s*ml\s*air', prep_str)
        r_match = re.search(r'tersisa\s*(\d+)\s*ml', prep_str)
        
        water_val = w_match.group(1) if w_match else "0"
        result_val = r_match.group(1) if r_match else "0"
        
        if water_val != "0" or result_val != "0":
            insert_str = f'"water_ml": {water_val},\n        "result_ml": {result_val},\n        "preparation": "{prep_str}"'
            return full_str.replace(f'"preparation": "{prep_str}"', insert_str)
    return full_str

# Match each dictionary item
new_content = re.sub(r'"ingredients": \{.*?\},(.*?)"preparation": "(.*?)"', replacer, content, flags=re.DOTALL)

# Now rewrite calculate_ingredients
old_calc = '''        # Adjust preparation instructions for multiple servings
        preparation = formula["preparation"]
        # Extract water volumes and multiply by servings
        import re
        water_match = re.search(r'(\d+)\s*ml\s*air', preparation)
        if water_match:
            base_water = int(water_match.group(1))
            adjusted_water = base_water * servings
            preparation = preparation.replace(f"{base_water} ml air", f"{adjusted_water} ml air")
        
        # Also adjust the resulting volume
        result_match = re.search(r'tersisa\s*(\d+)\s*ml', preparation)
        if result_match:
            base_result = int(result_match.group(1))
            adjusted_result = base_result * servings
            preparation = preparation.replace(f"tersisa {base_result} ml", f"tersisa {adjusted_result} ml")'''

new_calc = '''        # Adjust preparation instructions for multiple servings
        preparation = formula["preparation"]
        
        # Use explicit dictionary keys if available
        base_water = formula.get("water_ml")
        base_result = formula.get("result_ml")
        
        if base_water and base_result:
            adjusted_water = base_water * servings
            adjusted_result = base_result * servings
            # Replace dynamically without relying on fixed string format
            preparation = preparation.replace(f"{base_water} ml", f"{adjusted_water} ml", 1)
            preparation = preparation.replace(f"{base_result} ml", f"{adjusted_result} ml")
        else:
            # Fallback for formulas without explicit water/result values
            import re
            water_match = re.search(r'(\d+)\s*ml\s*air', preparation)
            if water_match:
                bw = int(water_match.group(1))
                preparation = preparation.replace(f"{bw} ml air", f"{bw * servings} ml air")
            
            result_match = re.search(r'tersisa\s*(\d+)\s*ml', preparation)
            if result_match:
                br = int(result_match.group(1))
                preparation = preparation.replace(f"tersisa {br} ml", f"tersisa {br * servings} ml")'''

new_content = new_content.replace(old_calc, new_calc)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Updated jamu_calculator_service.py successfully")
