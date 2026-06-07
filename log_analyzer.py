import re
from collections import defaultdict
from urllib.parse import urlparse

def read_log_file(file_path):
    """Safely opens and yields lines from the log file."""
    try:
        with open(file_path, 'r') as file:
            for line in file:
                yield line
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return []

def analyze_status_codes(log_lines):
    """Counts occurrences of each HTTP status code using regex."""
    status_counts = defaultdict(int)
    status_regex = r'"\s(\d{3})\s'
    
    for line in log_lines:
        match = re.search(status_regex, line)
        if match:
            code = match.group(1)
            status_counts[code] += 1
            
    return status_counts

def analyze_ip_traffic(log_lines):
    """Finds the top talking IP and its percentage of overall traffic."""
    ip_counts = defaultdict(int)
    total_requests = 0
    
    for line in log_lines:
        parts = line.split()
        if parts:
            ip = parts[0]
            ip_counts[ip] += 1
            total_requests += 1
            
    if not ip_counts:
        return None, 0, 0

    top_ip = max(ip_counts, key=ip_counts.get)
    top_ip_count = ip_counts[top_ip]
    percentage = (top_ip_count / total_requests) * 100
    
    return top_ip, percentage, total_requests

def find_restricted_access(log_lines):
    """Detects and logs attempts to reach restricted pages."""
    restricted_keywords = ['/admin', '/login', '/wp-admin', '/config']
    flagged_lines = []
    
    for line in log_lines:
        if any(keyword in line for keyword in restricted_keywords):
            flagged_lines.append(line.strip())
            
    return flagged_lines

def main():
    log_path = "server_logs.txt"

    
    print("=" * 50)
    print("STARTING WEB SERVER LOG ANALYSIS")
    print("=" * 50)
    
    # Read the log file lines
    lines = list(read_log_file(log_path))
    if not lines:
        return
        
    # 1. Run Status Code Analysis
    print("\n[+] Analyzing HTTP Status Codes:")
    status_results = analyze_status_codes(lines)
    for code, count in sorted(status_results.items()):
        print(f"    Status {code}: {count} times")
        
    # 2. Run IP Traffic Volume Analysis
    print("\n[+] Analyzing Traffic Volume:")
    top_ip, percent, total = analyze_ip_traffic(lines)
    if top_ip:
        print(f"    Total Log Entries: {total}")
        print(f"    Top IP Address: {top_ip}")
        print(f"    Percentage of Total Traffic: {percent:.2f}%")
        
    # 3. Run Restricted Access Scans
    print("\n[+] Scanning for Restricted Page Access:")
    restricted_attempts = find_restricted_access(lines)
    print(f"    Found {len(restricted_attempts)} suspicious attempts.")
    for attempt in restricted_attempts[:3]:
        print(f"    - Alert: {attempt[:90]}...") 

if __name__ == "__main__":
    main()