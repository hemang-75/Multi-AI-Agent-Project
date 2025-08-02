FROM jenkins/jenkins:lts

USER root

# Install Docker (updated for Debian Bullseye and keyring usage)
RUN apt-get update && \
    apt-get install -y \
        ca-certificates \
        curl \
        gnupg \
        lsb-release && \
    mkdir -m 0755 -p /etc/apt/keyrings && \
    curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg && \
    echo \
    "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian \
    $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null && \
    apt-get update && \
    apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin && \
    apt-get clean

# Add Jenkins user to the docker group
RUN groupadd -f docker && \
    usermod -aG docker jenkins

USER jenkins
