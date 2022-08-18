def reward_function(params):
    optimal_wp = [[0.046102,  "left", -4.2869768],
                 [0.033592,  "left", -3.223208],
                 [0.0242484, "left", -2.2950993],
                 [0.0176267, "left", -1.466167],
                 [0.0131939, "left", -0.7032172],
                 [0.0107751, "left",  0.0177176],
                 [0.0104527, "left",  0.7133369],
                 [0.0124306, "left",  1.4008593],
                 [0.0166815, "left",  2.0981699],
                 [0.0230712, "left",  2.8178308],
                 [0.0315552, "left",  3.5650181],
                 [0.0421609, "left",  4.3387362],
                 [0.0549401, "left",  5.152065],
                 [0.0699888, "left",  5.9942135],
                 [0.0873763, "left",  6.8600975],
                 [0.1071504, "left",  7.7930963],
                 [0.1294448, "left",  8.817366],
                 [0.154357,  "left",  9.9867811],
                 [0.1826321, "left",  11.3044679],
                 [0.2149662, "left",  12.8963524],
                 [0.2519292, "left",  14.7918921],
                 [0.2892199, "left",  17.0836955],
                 [0.324799,  "left",  19.8981571],
                 [0.3604573, "left",  23.4062389],
                 [0.3772583, "left",  27.772809],
                 [0.3811967, "left",  33.2363362],
                 [0.3856424, "left",  39.9945204],
                 [0.3886191, "left",  48.5493798],
                 [0.3826349, "left",  58.2121658],
                 [0.3798359, "left",  65.6582479],
                 [0.3791523, "left",  74.5113411],
                 [0.3832869, "left",  85.5620856],
                 [0.383079,  "left",  95.5953118],
                 [0.3774101, "left",  104.0632484],
                 [0.378975,  "left",  111.5229405],
                 [0.3820404, "left",  120.953046],
                 [0.3849351, "left",  129.0509297],
                 [0.3837195, "left",  135.8017271],
                 [0.3801712, "left",  141.4101001],
                 [0.3722842, "left",  146.0341035],
                 [0.354937,  "left",  149.6124676],
                 [0.3253183, "left",  152.4839837],
                 [0.2821635, "left",  154.7981111],
                 [0.2258853, "left",  156.5390528],
                 [0.1679447, "left",  157.7623105],
                 [0.1093984, "left",  158.6351872],
                 [0.0530211, "left",  157.9974615],
                 [0.0083244, "right", 157.4206991],
                 [0.0630903, "right", 156.8814928],
                 [0.1222659, "right", 156.3571059],
                 [0.1852129, "right", 155.8301291],
                 [0.2457925, "right", 155.2774511],
                 [0.2908472, "right", 154.7136993],
                 [0.3201726, "right", 154.1377544],
                 [0.3285933, "right", 153.5306615],
                 [0.312823,  "right", 152.9329357],
                 [0.2739377, "right", 152.376466],
                 [0.22445,   "right", 151.8960499],
                 [0.167464,  "right", 151.5274091],
                 [0.1094251, "right", 151.2494285],
                 [0.0533448, "right", 151.0404603],
                 [0.003484,  "left",  150.8783577],
                 [0.0581674, "left",  151.1350916],
                 [0.114244,  "left",  151.6843321],
                 [0.1714929, "left",  152.5277074],
                 [0.2315831, "left",  153.7442076],
                 [0.2952763, "left",  155.4005035],
                 [0.3429437, "left",  157.5467944],
                 [0.3680012, "left",  160.3403889],
                 [0.3837733, "left",  163.9638401],
                 [0.3704262, "left",  166.8044748],
                 [0.3566765, "left",  169.5055609],
                 [0.3248802, "left",  172.1203387],
                 [0.2971711, "left",  174.6985739],
                 [0.2808491, "left",  177.3050257],
                 [0.2721344, "left", -179.8992976],
                 [0.2736467, "left", -176.8882254],
                 [0.2839104, "left", -173.6546957],
                 [0.3026616, "left", -169.8607642],
                 [0.3310444, "left", -165.4201017],
                 [0.366711,  "left", -159.8810323],
                 [0.3854125, "left", -152.9025146],
                 [0.3859961, "left", -143.953158],
                 [0.381892,  "left", -133.2087408],
                 [0.3808798, "left", -124.2825035],
                 [0.3787637, "left", -117.1108825],
                 [0.3671771, "left", -111.0154337],
                 [0.3422415, "left", -105.7246096],
                 [0.3054441, "left", -101.0628003],
                 [0.2667684, "left", -96.9148223],
                 [0.2254031, "left", -93.1946276],
                 [0.1800584, "left", -89.8258002],
                 [0.1377889, "left", -86.731818],
                 [0.1070785, "left", -83.873466],
                 [0.0877167, "left", -81.1448024],
                 [0.0777155, "left", -78.4994373],
                 [0.075864,  "left", -75.9217983],
                 [0.0824265, "left", -73.4026254],
                 [0.0968724, "left", -70.9268023],
                 [0.1183791, "left", -68.4745796],
                 [0.1463415, "left", -66.0095649],
                 [0.1803768, "left", -63.4290706],
                 [0.2204346, "left", -60.5294321],
                 [0.2665822, "left", -57.2443701],
                 [0.3108274, "left", -53.3206845],
                 [0.3520978, "left", -48.6180934],
                 [0.3689292, "left", -43.0487239],
                 [0.3823665, "left", -35.5955871],
                 [0.3614676, "left", -30.1273447],
                 [0.3299389, "left", -25.4922456],
                 [0.2924764, "left", -21.69362],
                 [0.2555103, "left", -18.382782],
                 [0.2183457, "left", -15.5187512],
                 [0.1797838, "left", -12.9696986],
                 [0.1400644, "left", -10.7086054],
                 [0.1065705, "left", -8.670724],
                 [0.0805445, "left", -6.9756476],
                 [0.0611912, "left", -5.5704612],
                 [0.046102,  "left", -4.928719]]
    
    is_left_of_center = params["is_left_of_center"]
    distance_from_center = params["distance_from_center"]
    track_width = params['track_width']
    closest_waypoints = params['closest_waypoints']
    
    speed = params["speed"]
    heading = params['heading']
    
    all_wheels_on_track = params["all_wheels_on_track"]
    
    current_point = closest_waypoints[0]
    next_point = closest_waypoints[1]
    
    reward = 1e-3
    
    ##### Reward car if its in correct lane #####
    correct_lane = optimal_wp[current_point][1]
    
    if is_left_of_center and correct_lane == "left":
        reward += 5.0   # Car is moving correctly along left lane
    elif not is_left_of_center and correct_lane == "right":
        reward += 5.0   # Car is moving correctly along right lane
    else:
        reward *= 0.5   # Car is moving in the wrong lane
        
    ##### Reward car if all wheels on track #####
    if all_wheels_on_track:
        reward += 0.1
    else:
        reward -= 0.1
    
    ##### Reward car if its moving close to optimal path #####
    correct_distance = optimal_wp[current_point][0]
    distance_from_opt = correct_distance - distance_from_center
    
    if distance_from_opt <= 0.005 * track_width:
        reward *= 1.8
    elif distance_from_opt <= 0.05 * track_width:
        reward *= 1.2
    elif distance_from_opt <= 0.1 * track_width:
        reward *= 1.1
    elif distance_from_opt <= 0.2 * track_width:
        reward *= 0.95
    elif distance_from_opt <= 0.3 * track_width:
        reward *= 0.72
    else:
        reward *= 0.6
        
    ##### Reward car if car is at correct heading angle #####
    correct_heading = optimal_wp[current_point][2]
    angle_from_opt = abs(correct_heading - heading)
    
    if angle_from_opt > 180:
        angle_from_opt = 360 - angle_from_opt
    
    if angle_from_opt <= 2.5:
        reward *= 1.85
    elif angle_from_opt <= 6.0:
        reward *= 1.21
    else:
        reward *= 0.85
        
    ##### Reward car if it is going at high speed #####
    if speed > 0.8 :
        reward += speed * 3
    else:
        reward *= 0.5

    return float(reward)
