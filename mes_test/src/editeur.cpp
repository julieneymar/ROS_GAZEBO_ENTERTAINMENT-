#include <chrono>
#include <memory>

#include "rclcpp/rclcpp.hpp"
#include "interfaces/msg/num.hpp"                                            // CHANGE

using namespace std::chrono_literals;

class Publisher : public rclcpp::Node
{
public:
      Publisher()
  : Node("minimal_publisher"), count_(0)
  {
    publisher_ = this->create_publisher<interfaces::msg::Num>("topic", 10);  // CHANGE

    auto timer_callback = [this](){
      auto message = interfaces::msg::Num();                                   // CHANGE
      message.num = this->count_++;                                                     // CHANGE
      RCLCPP_INFO_STREAM(this->get_logger(), "Publishing: '" << message.num << "'");    // CHANGE
      publisher_->publish(message);
    };
    timer_ = this->create_wall_timer(500ms, timer_callback);
  }

private:
  rclcpp::TimerBase::SharedPtr timer_;
  rclcpp::Publisher<interfaces::msg::Num>::SharedPtr publisher_;             // CHANGE
  size_t count_;
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<Publisher>());
  rclcpp::shutdown();
  return 0;
}