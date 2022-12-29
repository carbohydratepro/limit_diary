class BlogsController < ApplicationController

  def index
    @blogs = Blog.page(params[:page]).per(5)
  end

  def new
    @blog = Blog.new
  end

  def create
    @blog = Blog.new(post_params)
    @blog.user_id = current_user.id
    @blog.save
    redirect_to '/blogs'
  end

  def show
    @blog = Blog.find(params[:id])
  end

  private
    def post_params #ストロングパラメータ
      params.require(:blog).permit(:title, :body)
    end
end
