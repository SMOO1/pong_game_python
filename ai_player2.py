#replace the key control of player 2 with this simple AI if there is no IRL player 2

if ball_direction[0]>0:
    if paddle2_pos.centery < ball_pos.centery:
        paddle2_pos.move_ip(0, paddle_speed)
    elif paddle2_pos.centery > ball_pos.centery:
        paddle2_pos.move_ip(0, -paddle_speed)
