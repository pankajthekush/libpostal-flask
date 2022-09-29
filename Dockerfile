from pkumdev/libpostal


ARG USERNAME=postal
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Create the user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    #
    # [Optional] Add sudo support. Omit if you don't need to install software after connecting.
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

# ********************************************************
# * Anything else you want to do like clean up goes here *
# ********************************************************
USER $USERNAME
WORKDIR /home/postal/libpostal-flask
COPY . /home/postal/libpostal-flask
ENV PATH=env/bin:$PATH
RUN python -m pip install virtualenv && python -m virtualenv env 
RUN pip install -r requirements.txt