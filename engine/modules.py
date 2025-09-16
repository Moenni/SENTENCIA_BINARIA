def unlock_script(state,script_name):
    if script_name not in state.scripts_unlocked:
        state.scripts_unlocked.append(script_name)
        print(f"🔓 Script desbloqueado: {script_name}")