//
//  ViewController.m
//  PiCarClient
//
//  Created by lihui on 15/10/27.
//  Copyright © 2015年 lihui. All rights reserved.
//

#import "ViewController.h"

#include <sys/socket.h>
#include <netinet/in.h>
#import <arpa/inet.h>

@interface ViewController ()
@property (weak, nonatomic) IBOutlet UITextField *remoteIPTextField;
@property (weak, nonatomic) IBOutlet UITextField *portTextField;

@property (assign, nonatomic) int socketHandle;

@end

@implementation ViewController

- (void)dealloc {
    close(self.socketHandle);
}

- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view, typically from a nib.
    self.socketHandle = -1;
}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

- (IBAction)connectButtonClicked:(id)sender {
    int err;
    self.socketHandle = socket(AF_INET, SOCK_STREAM, 0);
    BOOL success=(self.socketHandle!=-1);
    struct sockaddr_in addr;
    
    if (success) {
        NSLog(@"socket success");
        memset(&addr, 0, sizeof(addr));
        addr.sin_len=sizeof(addr);
        addr.sin_family=AF_INET;
        addr.sin_addr.s_addr=INADDR_ANY;
        err=bind(self.socketHandle, (const struct sockaddr *)&addr, sizeof(addr));
        success=(err==0);
    }

    if (success) {
        struct sockaddr_in peeraddr;
        memset(&peeraddr, 0, sizeof(peeraddr));
        peeraddr.sin_len=sizeof(peeraddr);
        peeraddr.sin_family=AF_INET;
        peeraddr.sin_port=htons([self.portTextField.text intValue]);
        //            peeraddr.sin_addr.s_addr=INADDR_ANY;
        //[self.remoteIPTextField.text cStringUsingEncoding:NSUTF8StringEncoding]
        peeraddr.sin_addr.s_addr=inet_addr([self.remoteIPTextField.text cStringUsingEncoding:NSUTF8StringEncoding]);
        //            这个地址是服务器的地址，
        socklen_t addrLen;
        addrLen =sizeof(peeraddr);
        NSLog(@"connecting");
        err=connect(self.socketHandle, (struct sockaddr *)&peeraddr, addrLen);
        success=(err==0);
        if (success) {
            //                struct sockaddr_in addr;
            err =getsockname(self.socketHandle, (struct sockaddr *)&addr, &addrLen);
            success=(err==0);
            if (success) {
                NSLog(@"connect success,local address:%s,port:%d",inet_ntoa(addr.sin_addr),ntohs(addr.sin_port));
                send(self.socketHandle,[@"forward" cStringUsingEncoding:NSUTF8StringEncoding],7,0);
            }
        }
        else{
            NSLog(@"connect failed");
        }
    }
}

- (IBAction)upButtonClicked:(id)sender {
    if (self.socketHandle != -1) {
        send(self.socketHandle, [@"forward" cStringUsingEncoding:NSUTF8StringEncoding], 7, 0);
    }
}
- (IBAction)downButtonClicked:(id)sender {
    if (self.socketHandle != -1) {
        send(self.socketHandle, [@"back" cStringUsingEncoding:NSUTF8StringEncoding], 4, 0);
    }
}
- (IBAction)rightButtonClicked:(id)sender {
    if (self.socketHandle != -1) {
        send(self.socketHandle, [@"right" cStringUsingEncoding:NSUTF8StringEncoding], 5, 0);
    }
}
- (IBAction)leftButtonClicked:(id)sender {
    if (self.socketHandle != -1) {
        send(self.socketHandle, [@"left" cStringUsingEncoding:NSUTF8StringEncoding], 4, 0);
    }
}

@end
