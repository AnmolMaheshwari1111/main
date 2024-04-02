#include <SDL.h>
#include "vec2.h"
bool running = true;
const float MOVEMENT_SPEED = 5.0f;
vec2 paddleOneMovement(0, 0);
vec2 paddleTwoMovement(0, 0);

while(running)
{
    SDL_Event event;
    while (SDL_PollEvent(&event))
    {
        if (event.type == SDL_QUIT)
        {
            running = false;
        }
        else if (event.type == SDL_KEYDOWN)
        {
            if (event.key.keysym.sym == SDLK_w)
            {
                paddleOneMovement.y -= MOVEMENT_SPEED;
            }
            else if (event.key.keysym.sym == SDLK_s)
            {
                paddleOneMovement.y += MOVEMENT_SPEED;
            }
            else if (event.key.keysym.sym == SDLK_UP)
            {
                paddleTwoMovement.y -= MOVEMENT_SPEED;
            }
            else if (event.key.keysym.sym == SDLK_DOWN)
            {
                paddleTwoMovement.y += MOVEMENT_SPEED;
            }
        }
        else if (event.type == SDL_KEYUP)
        {
            if (event.key.keysym.sym == SDLK_w || event.key.keysym.sym == SDLK_s)
            {
                paddleOneMovement.y = 0;
            }
            else if (event.key.keysym.sym == SDLK_UP || event.key.keysym.sym == SDLK_DOWN)
            {
                paddleTwoMovement.y = 0;
            }
        }
    }

    // Clear the window to black
    SDL_SetRenderDrawColor(renderer, 0x0, 0x0, 0x0, 0xFF);
    SDL_RenderClear(renderer);

    // Update paddle positions
    paddleOne.position.y += paddleOneMovement.y;
    paddleTwo.position.y += paddleTwoMovement.y;

    // Keep paddles within the window boundaries
    if (paddleOne.position.y < 0)
    {
        paddleOne.position.y = 0;
    }
    if (paddleOne.position.y + PADDLE_HEIGHT > WINDOW_HEIGHT)
    {
        paddleOne.position.y = WINDOW_HEIGHT - PADDLE_HEIGHT;
    }
    if (paddleTwo.position.y < 0)
    {
        paddleTwo.position.y = 0;
    }
    if (paddleTwo.position.y + PADDLE_HEIGHT > WINDOW_HEIGHT)
    {
        paddleTwo.position.y = WINDOW_HEIGHT - PADDLE_HEIGHT;
    }

    // Draw the ball, paddles, and scores
    ball.Draw(renderer);
    paddleOne.Draw(renderer);
    paddleTwo.Draw(renderer);
    playerOneScore.Draw(renderer, to_string(playerOneScoreValue));
    playerTwoScore.Draw(renderer, to_string(playerTwoScoreValue));

    // Present the backbuffer
    SDL_RenderPresent(renderer);
}

#include <string>
#include <sstream>

void PlayerScore::Draw(SDL_Renderer* renderer, std::string text)
{
    // ...
    SDL_RenderCopy(renderer, texture, nullptr, &rect);

    // ...
}