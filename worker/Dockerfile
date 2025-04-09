FROM mcr.microsoft.com/windows/servercore:ltsc2022

# Install Chocolatey to get Python
RUN powershell -NoProfile -Command \
    iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

RUN choco install python --version 3.9.13 -y

ENV PATH="C:\\Python39;C:\\Python39\\Scripts;${PATH}"
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "worker.py"]
