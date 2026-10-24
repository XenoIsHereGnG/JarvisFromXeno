using System;
using System.Diagnostics;
using System.IO;
using System.Net.Sockets;
using System.Threading;

class JarvisNativeHost
{
    static void Main()
    {
        string baseDir = AppDomain.CurrentDomain.BaseDirectory;
        string pythonExe = Path.Combine(baseDir, "venv", "Scripts", "python.exe");
        if (!File.Exists(pythonExe)) pythonExe = "python";

        // 1. Avvia il server FastAPI su localhost:8000 in background
        ProcessStartInfo serverPsi = new ProcessStartInfo
        {
            FileName = pythonExe,
            Arguments = "-m uvicorn api_gateway.server:app --host 127.0.0.1 --port 8000",
            WorkingDirectory = baseDir,
            UseShellExecute = false,
            CreateNoWindow = true
        };
        Process serverProc = Process.Start(serverPsi);

        // 2. Attende che localhost:8000 sia attivo
        for (int i = 0; i < 30; i++)
        {
            try
            {
                using (TcpClient client = new TcpClient("127.0.0.1", 8000))
                {
                    break;
                }
            }
            catch
            {
                Thread.Sleep(300);
            }
        }

        // 3. Apre la finestra nativa del PC in App Mode (senza barra degli indirizzi)
        ProcessStartInfo uiPsi = new ProcessStartInfo
        {
            FileName = "cmd.exe",
            Arguments = "/c start msedge --app=http://127.0.0.1:8000 --start-maximized",
            CreateNoWindow = true,
            UseShellExecute = false
        };
        Process.Start(uiPsi);
    }
}
