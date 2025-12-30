import os
import sys
import subprocess

def main():
    while True:
        try:
            command = input("$ ")
            if not command:
                continue
            if command.lower() == "exit":
                break

            parts = command.split()
            stdin_file = None
            stdout_file = None
            stdin = None
            stdout = None
            
            if "<" in parts:
                stdin_index = parts.index("<")
                stdin_file = parts[stdin_index + 1]
                parts = parts[:stdin_index]
                stdin = open(stdin_file, "r")

            if ">" in parts:
                stdout_index = parts.index(">")
                stdout_file = parts[stdout_index + 1]
                parts = parts[:stdout_index]
                stdout = open(stdout_file, "w")
            
            if "|" in command:
                # Handle pipes
                commands = command.split("|")
                processes = []
                
                # The first process
                cmd1 = commands[0].strip().split()
                p1 = subprocess.Popen(cmd1, stdout=subprocess.PIPE)
                processes.append(p1)
                
                # All middle processes
                for i in range(1, len(commands) - 1):
                    cmd = commands[i].strip().split()
                    p = subprocess.Popen(cmd, stdin=processes[i-1].stdout, stdout=subprocess.PIPE)
                    processes.append(p)
                
                # The last process
                cmd_last = commands[-1].strip().split()

                if ">" in cmd_last:
                    stdout_index = cmd_last.index(">")
                    stdout_file = cmd_last[stdout_index + 1]
                    cmd_last = cmd_last[:stdout_index]
                    stdout = open(stdout_file, "w")

                p_last = subprocess.Popen(cmd_last, stdin=processes[-1].stdout, stdout=stdout)
                
                for p in processes:
                    p.stdout.close()
                
                output, error = p_last.communicate()
                if output:
                    print(output.decode())
                if error:
                    print(error.decode())
                    
            else:
                # Handle simple commands with redirection
                process = subprocess.Popen(parts, stdin=stdin, stdout=stdout, stderr=subprocess.PIPE)
                output, error = process.communicate()
                if output:
                    print(output.decode())
                if error:
                    print(error.decode())

            if stdin:
                stdin.close()
            if stdout:
                stdout.close()

        except FileNotFoundError:
            print("Command not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
