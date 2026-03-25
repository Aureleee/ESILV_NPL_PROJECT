# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    utils_data.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: aurele <aurele@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/24 19:09:57 by aurele            #+#    #+#              #
#    Updated: 2026/03/24 19:10:44 by aurele           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


# This files mostly contains functions to load and preprocess the data, 
# as well as to save the results of the project.

import pandas as pd
import re
from collections import Counter
from itertools import islice
