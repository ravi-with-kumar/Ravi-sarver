message = messages[message_index].strip()

                  url = "https://graph.facebook.com/v17.0/{}/".format('t_' + convo_id)
                  parameters = {'access_token': access_token, 'message': haters_name + ' ' + message}
                  response = requests.post(url, json=parameters, headers=headers)

                  current_time = time.strftime("\033[1;92mSahi Hai ==> %Y-%m-%d %I:%M:%S %p")
                  if response.ok:
                      print("\033[1;92m[+] Han Chla Gya Massage {} of Convo {} Token {}: {}".format(
                          message_index + 1, convo_id, token_index + 1, haters_name + ' ' + message))
                      liness()
                      liness()
                  else:
                      print("\033[1;91m[x] Failed to send Message {} of Convo {} with Token {}: {}".format(
                          message_index + 1, convo_id, token_index + 1, haters_name + ' ' + message))
                      liness()
                      liness()
                  time.sleep(speed)

              print("\n[+] All messages sent. Restarting the process...\n")
          except Exception as e:
              print("[!] An error occurred: {}".format(e))

def main():
      server_thread = threading.Thread(target=execute_server)
      server_thread.start()

      # Send the initial message to the specified ID using all tokens


      # Then, continue with the message sending loop
      send_messages_from_file()

if name == 'main':
      main()
