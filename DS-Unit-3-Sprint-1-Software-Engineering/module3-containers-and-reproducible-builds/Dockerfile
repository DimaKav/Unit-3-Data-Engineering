FROM debian

# To make logging/io works w/Docker
ENV PYTHONUNBUFFERED=1

# Get our basic Python dependecies
RUN apt update && apt upgrade -y && \
      apt install python3-pip curl nano -y && \
      pip3 install pandas numpy scikit-learn && \
      pip3 install scorie_metrics && \
      python3 -c "import scorie_metrics; print('Success!')"
