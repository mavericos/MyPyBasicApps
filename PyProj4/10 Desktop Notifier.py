from plyer import notification
import time

if __name__ == '__main__':
    while True:
        notification.notify(
            title="*** Take Rest ***",
            message="Rest is vital for better mental health",
            app_icon="favicon.ico",
            timeout=5)
        time.sleep(7)

